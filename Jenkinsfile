pipeline {
  agent { label 'jenkins-slave-linux-cu01use1gs1jx01' }
  
  parameters {
        text(name: 'AWS Environment', defaultValue: '', description: 'Specify one or more of the following. If more than one environment is required, separate each environment with a line break:\n\nDeltekdev\nFlexplus\nCostpoint\nDCO\nOffsec\nGovwinProduction\nGovwinDev\nInterspec\nEspecs\nArcom\nDeltekEA\nOnvia\nGlobalOSS\nECMaconomy\nSecuritySandbox\nDeliverySandbox\nUnionpoint\nServiceBroker\nArchsandbox\nSC-Vantagepoint\nEC-MGT\nPieterEerlings\nsc-dhtmlx\nsc-ssec\nec-ssec')
        string(name: 'Username', defaultValue: '', description: '')
        string(name: 'Email', defaultValue: '', description: '')
        string(name: 'Employee ID', defaultValue: '', description: '')
        string(name: 'ServiceNow Case', defaultValue: '', description: '')
    }

    stages {
        stage('Checkout Source') {
            steps {
                sh 'python3 --version'
                sh 'pip3 install boto3'
                sh 'pip3 install EmailMessage'
                checkout([$class: 'GitSCM', branches: [[name: "*/master"]], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: "https://github.com/JohnVincentAgbayani/AWS-AccountManagement.git"]]])
            }
        }
        stage('Execute Shell') {
            steps {
                script {
                    def awsCredential = null
                    
                    def awsEnvironment = "${params['AWS Environment']}"
                    def awsEnvSplit = awsEnvironment.split('\n')
                    currentBuild.displayName = "${params['ServiceNow Case']}"
                    
                    for (env in awsEnvSplit){
                        env = env.replaceAll("\\s","")
                        sh "echo ${env} > temp_env.txt"
                    
                        
                        if(env=="Deltekdev"){
                            awsCredential = 'infra-at-dev'
                        }
                        else if(env=="Flexplus"){
                            awsCredential = 'infra-at-flexplus'
                        }
                        else if(env=="Costpoint"){
                            awsCredential = 'infra-at-costpoint'
                        }
                        else if(env=="DCO"){
                            awsCredential = 'infra-at-dco'
                        }
                        else if(env=="Offsec"){
                            awsCredential = 'infra-at-offsec'
                        }
                        else if(env=="GovwinProduction"){
                            awsCredential = 'infra-at-govwinpd'
                        }
                        else if(env=="GovwinDev"){
                            awsCredential = 'infra-at-govwindv'
                        }
                        else if(env=="Interspec"){
                            awsCredential = 'infra-at-interspec'
                        }
                        else if(env=="Especs"){
                            awsCredential = 'infra-at-especs'
                        }
                        else if(env=="Arcom"){
                            awsCredential = 'infra-at-arcom'
                        }
                        else if(env=="DeltekEA"){
                            awsCredential = 'infra-at-deltekea'
                        }
                        else if(env=="Onvia"){
                            awsCredential = 'infra-at-onvia'
                        }
                        else if(env=="GlobalOSS"){
                            awsCredential = 'infra-at-oss'
                        }
                        else if(env=="ECMaconomy"){
                            awsCredential = 'infra-at-ecmaconomy'
                        }
                        else if(env=="SecuritySandbox"){
                            awsCredential = 'infra-at-secsandbox'
                        }
                        else if(env=="DeliverySandbox"){
                            awsCredential = 'infra-at-delsandbox'
                        }
                        else if(env=="Unionpoint"){
                            awsCredential = 'infra-at-unionpoint'
                        }
                        else if(env=="ServiceBroker"){
                            awsCredential = 'infra-at-servicebroker'
                        }
                        else if(env=="Archsandbox"){
                            awsCredential = 'infra-at-archsandbox'
                        }
                        else if(env=="SC-Vantagepoint"){
                            awsCredential = 'infra-at-sc-vantagepoint'
                        }
                        else if(env=="EC-MGT"){
                            awsCredential = 'infra-at-ec-mgt'
                        }
                        else if(env=="PieterEerlings"){
                            awsCredential = 'infra-at-pieter-eerlings'
                        }
                        else if(env=="sc-dhtmlx"){
                            awsCredential = 'infra-at-sc-dhtmlx'
                        }
                        else if(env=="sc-ssec"){
                            awsCredential = 'infra-at-sc-ssec'
                        }
                        else if(env=="ec-ssec"){
                            awsCredential = 'infra-at-ec-ssec'
                        }
                            
                        withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',credentialsId: "${awsCredential}", accessKeyVariable: 'AWS_ACCESS_KEY_ID', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
                            sh "python3 create_user.py"
                        }
                    }
                }
            }
        }
    }
}