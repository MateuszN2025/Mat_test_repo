import com.cloudbees.plugins.credentials.SystemCredentialsProvider
import com.cloudbees.plugins.credentials.domains.Domain
import jenkins.model.Jenkins

def jenkins = Jenkins.get()
def nodeName = 'local-pc-ssh'
def credentialId = 'local-pc-ssh-key'

def existingNode = jenkins.getNode(nodeName)
if (existingNode != null) {
	jenkins.removeNode(existingNode)
	println("Removed disabled SSH agent '${nodeName}'")
} else {
	println("SSH agent bootstrap disabled: '${nodeName}' not present")
}

def store = SystemCredentialsProvider.instance.store
def domain = Domain.global()
def existingCredential = SystemCredentialsProvider.instance.credentials.find { it.id == credentialId }
if (existingCredential != null) {
	store.removeCredentials(domain, existingCredential)
	println("Removed disabled SSH credential '${credentialId}'")
}

return