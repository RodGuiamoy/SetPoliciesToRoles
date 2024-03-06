// def environment = ""
// def credentialsId = ""
// def policyARNs = ""
// def roleName = ""


class rolesToPoliciesObj {
    String environment
    String policyNames
    String policyARNs
    String roleName
}

def rolesToPoliciesObjs = []

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
        stage('Read CSV') {
            steps {
                script {
                    def csvData = sh(script: 'python3 read_csv.py', returnStdout: true).trim()

                    def rows = csvData.split('\n')
                    row = rows.drop(1)

                    rows.each { row ->

                        // Define the regular expression pattern
                        def pattern = /'([^']*)'/

                        // Find all matches using the pattern
                        def matcher = (row =~ pattern)

                        // rolesToPoliciesObjs << new rolesToPoliciesObj(environment: matcher[0][1], policyNames: matcher[1][1], policyARNs: "", roleName: matcher[2][1])

                        //echo "${matcher[0]}"
                        // Iterate over matches and print captured groups

                        def environment = ""
                        def policyNames = ""
                        def roleName = ""

                        int ctr = 0
                        matcher.each { match ->
                            if (ctr == 0) {
                                environment = match[1]
                            }
                            else if (ctr == 1) {
                                policyNames = match[1]
                            }
                            else if (ctr == 2) {
                                roleName = match[1]
                            }

                            ctr++
                        }

                        echo "${environment}"
                        echo "${policyNames}" 
                        echo "${roleName}"
                        
                    }

                    // echo "${rolesToPoliciesObjs}"
                }
            }
        }
        // stage('GetEnvironmentDetails') {
        //     steps {
        //         script {
        //             environment = params.Environment

        //             switch (environment) {
        //                 case 'rod_aws':
        //                     credentialsId = 'rod_aws'
        //                     break
        //                 default:
        //                     error("No matching environment details found that matches \"${environment}\".")
        //             }

        //             echo "Successfully retrieved environment details for environment \"${environment}\"."          
        //         }
        //     }
        // }
        // stage('GetPolicyARNs') {
        //     steps {
        //         script {
        //             policyNames = params.PolicyNames

        //             echo "${policyNames}"

        //             withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',credentialsId: "${credentialsId}", accessKeyVariable: 'AWS_ACCESS_KEY_ID', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
                        
        //                 def cmd = "python3 1_get_policy_arns.py '${policyNames}'"

        //                 // Executes the AWS CLI command and does some post-processing.
        //                 // The output includes the command at the top and can't be parsed so we have to drop the first line
        //                 policyARNs = sh(script: cmd, returnStdout: true).trim()
        //                 // cmdOutput = cmdOutput.readLines().drop(1).join("\n")
                        
        //                 echo "${policyARNs}"
        //             }
                    
        //         }
        //     }
        // }
        // stage('CreateRole') {
        //     steps {
        //         script {
        //             roleName = params.RoleName

        //             echo "${roleName}"

        //             withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',credentialsId: "${credentialsId}", accessKeyVariable: 'AWS_ACCESS_KEY_ID', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
        //                 sh "python3 2_create_role.py '${roleName}'"
        //             }
                    
        //         }
        //     }
        // }
        // stage('AttachPoliciesToRoles') {
        //     steps {
        //         script {

        //             withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',credentialsId: "${credentialsId}", accessKeyVariable: 'AWS_ACCESS_KEY_ID', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
        //                 sh "python3 3_attach_policies_to_role.py '${roleName}' '${policyARNs}'"
        //             }
                    
        //         }
        //     }
        // }
    }
}

