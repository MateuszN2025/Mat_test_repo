import hudson.security.HudsonPrivateSecurityRealm
import jenkins.model.Jenkins

def instance = Jenkins.get()
def adminId = System.getenv('JENKINS_ADMIN_ID')
def adminPassword = System.getenv('JENKINS_ADMIN_PASSWORD')

if (!adminId || !adminPassword) {
	println('Skipping admin bootstrap: missing JENKINS_ADMIN_ID or JENKINS_ADMIN_PASSWORD')
	return
}

def realm = instance.getSecurityRealm()
if (!(realm instanceof HudsonPrivateSecurityRealm)) {
	println('Skipping admin bootstrap: security realm is not HudsonPrivateSecurityRealm')
	return
}

def existingUser = realm.getUser(adminId)
if (existingUser == null) {
	realm.createAccount(adminId, adminPassword)
	println("Created Jenkins admin user '${adminId}' from environment")
} else {
	def details = existingUser.getProperty(HudsonPrivateSecurityRealm.Details)
	if (details == null || !details.isPasswordCorrect(adminPassword)) {
		def fromPlainPassword = HudsonPrivateSecurityRealm.Details.class.getDeclaredMethod('fromPlainPassword', String)
		fromPlainPassword.setAccessible(true)
		existingUser.addProperty(fromPlainPassword.invoke(null, adminPassword))
		existingUser.save()
		println("Updated Jenkins admin password for '${adminId}' from environment")
	}
}
