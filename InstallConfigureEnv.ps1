Get-ExecutionPolicy
Set-ExecutionPolicy AllSigned; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
choco -?
choco install git -y
choco install openssh -y -params "\SSHAgentFeature"
choco install nodejs npm -y
npm
choco install atom -y
choco install python2 -y
choco install awscli -y
choco install unzip Less -y
