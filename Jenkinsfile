pipeline {
  agent { label 'jenkins-slave-linux-cu01use1gs1jx01' }
  
  parameters {
        // text(name: 'AWS Environment', defaultValue: '', description: 'Specify one or more of the following. If more than one environment is required, separate each environment with a line break:\n\nDeltekdev\nFlexplus\nCostpoint\nDCO\nOffsec\nGovwinProduction\nGovwinDev\nInterspec\nEspecs\nArcom\nDeltekEA\nOnvia\nGlobalOSS\nECMaconomy\nSecuritySandbox\nDeliverySandbox\nUnionpoint\nServiceBroker\nArchsandbox\nSC-Vantagepoint\nEC-MGT\nPieterEerlings\nsc-dhtmlx\nsc-ssec\nec-ssec')
        // string(name: 'Username', defaultValue: '', description: '')
        // string(name: 'Email', defaultValue: '', description: '')
        // string(name: 'Employee ID', defaultValue: '', description: '')
        // string(name: 'ServiceNow Case', defaultValue: '', description: '')
        string(name: 'Environment', defaultValue: 'rod_aws', description: '')
    }

    def environment = ""
    def credentialsId = ""

    stages {
        stage('Checkout Source') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: "*/main"]], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: "https://github.com/RodGuiamoy/SetPoliciesToRoles.git"]]])
            }
        }
        stage('GetEnvironmentDetails') {
            steps {
                script {
                    environment = params.Environment

                    switch (environment) {
                        case 'rod_aws':
                            credentialsId = '554249804926'
                            break
                        default:
                            error("No matching environment details found that matches \"${environment}\".")
                    }

                        echo "Successfully retrieved environment details for environment \"${environment}\"."          
                }
            }
        }
    }
}
