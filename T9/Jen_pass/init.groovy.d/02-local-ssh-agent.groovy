import com.cloudbees.jenkins.plugins.sshcredentials.impl.BasicSSHUserPrivateKey
import com.cloudbees.plugins.credentials.CredentialsScope
import com.cloudbees.plugins.credentials.SystemCredentialsProvider
import com.cloudbees.plugins.credentials.domains.Domain
import hudson.model.Node
import hudson.plugins.sshslaves.SSHLauncher
import hudson.plugins.sshslaves.verifiers.NonVerifyingKeyVerificationStrategy
import hudson.slaves.DumbSlave
import hudson.slaves.RetentionStrategy
import jenkins.model.Jenkins

def jenkins = Jenkins.get()
def nodeName = 'local-pc-ssh'
def obsoleteNodeName = 'autotest_agent'
def credentialId = 'local-pc-ssh-key'
def username = 'mniedziolka'
def host = '172.28.221.58'
def remoteRoot = '/home/mniedziolka/jenkins-agent'
def labels = 'local-pc ssh-agent'
def javaPath = '/usr/lib/jvm/java-21-openjdk-amd64/bin/java'
def keyFile = new File('/var/jenkins_home/.ssh/id_ed25519_agent')

if (!keyFile.exists()) {
	println("Skipping SSH agent bootstrap: missing ${keyFile}")
	return
}

def store = SystemCredentialsProvider.instance.store
def domain = Domain.global()
def existingCredential = SystemCredentialsProvider.instance.credentials.find { it.id == credentialId }
if (existingCredential != null) {
	store.removeCredentials(domain, existingCredential)
}

def obsoleteNode = jenkins.getNode(obsoleteNodeName)
if (obsoleteNode != null) {
	jenkins.removeNode(obsoleteNode)
	println("Removed obsolete Jenkins node '${obsoleteNodeName}'")
}

def credential = new BasicSSHUserPrivateKey(
	CredentialsScope.GLOBAL,
	credentialId,
	username,
	new BasicSSHUserPrivateKey.DirectEntryPrivateKeySource(keyFile.text),
	'',
	'Local host SSH key for Jenkins agent'
)
store.addCredentials(domain, credential)

def existingNode = jenkins.getNode(nodeName)
if (existingNode != null) {
	jenkins.removeNode(existingNode)
}

def launcher = new SSHLauncher(
	host,
	22,
	credentialId,
	null,
	javaPath,
	null,
	null,
	60,
	3,
	10,
	new NonVerifyingKeyVerificationStrategy()
)

def node = new DumbSlave(
	nodeName,
	'Local PC SSH agent',
	remoteRoot,
	'1',
	Node.Mode.NORMAL,
	labels,
	launcher,
	new RetentionStrategy.Always(),
	[]
)

jenkins.addNode(node)
println("Created Jenkins SSH agent '${nodeName}'")

def computer = jenkins.getNode(nodeName)?.toComputer()
if (computer != null) {
	computer.connect(true)
	println("Triggered SSH connection for '${nodeName}'")
}