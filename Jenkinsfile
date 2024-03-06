def environment = ""
def credentialsId = ""
def policyARNs = ""
def roleName = ""


pipeline {
  agent { label 'jenkins-slave-linux-cu01use1gs1jx01' }
  
  parameters {
        // text(name: 'AWS Environment', defaultValue: '', description: 'Specify one or more of the following. If more than one environment is required, separate each environment with a line break:\n\nDeltekdev\nFlexplus\nCostpoint\nDCO\nOffsec\nGovwinProduction\nGovwinDev\nInterspec\nEspecs\nArcom\nDeltekEA\nOnvia\nGlobalOSS\nECMaconomy\nSecuritySandbox\nDeliverySandbox\nUnionpoint\nServiceBroker\nArchsandbox\nSC-Vantagepoint\nEC-MGT\nPieterEerlings\nsc-dhtmlx\nsc-ssec\nec-ssec')
        // string(name: 'Username', defaultValue: '', description: '')
        // string(name: 'Email', defaultValue: '', description: '')
        // string(name: 'Employee ID', defaultValue: '', description: '')
        // string(name: 'ServiceNow Case', defaultValue: '', description: '')
        string(name: 'Environment', defaultValue: 'rod_aws', description: '')
        string(name: 'RoleName', defaultValue: 'rod_test_00', description: '')
        string(name: 'PolicyNames', defaultValue: 'AMICreationAssumeRole,AMICreationPolicy,NonExistentPolicy', description: '')
    }



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
                            credentialsId = 'rod_aws'
                            break
                        default:
                            error("No matching environment details found that matches \"${environment}\".")
                    }

                    echo "Successfully retrieved environment details for environment \"${environment}\"."          
                }
            }
        }
        stage('GetPolicyARNs') {
            steps {
                script {
                    policyNames = params.PolicyNames

                    echo "${policyNames}"

                    withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',credentialsId: "${credentialsId}", accessKeyVariable: 'AWS_ACCESS_KEY_ID', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
                        sh "python3 1_get_policy_arns.py '${policyNames}'"
                    }
                    
                }
            }
        }
        stage('CreateRole') {
            steps {
                script {
                    roleName = params.RoleName

                    echo "${roleName}"

                    withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',credentialsId: "${credentialsId}", accessKeyVariable: 'AWS_ACCESS_KEY_ID', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
                        sh "python3 2_create_role.py '${roleName}'"
                    }
                    
                }
            }
        }
    }
}
