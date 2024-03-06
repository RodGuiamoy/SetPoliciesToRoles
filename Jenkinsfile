// def environment = ""
// def credentialsId = ""
// def policyARNs = ""


// // Function to find region by prefix for non-goss AWS accounts
// def findEnvironmentCredentialsId(String environment, List<environmentCredentialIDs> environmentCredentialIDs) {
//     for (environmentCredentialID in environmentCredentialIDs) {
//         if (environment == environmentCredentialIDs.environment) {
//             return environmentCredentialIDs.credentialId
//         }
//     }
//     return null
// }


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

                    rows.each { row ->
                        row = row.replaceAll("\\s", "")

                        // Define the regular expression pattern
                        def pattern = /'([^']*)'/

                        // Find all matches using the pattern
                        def matcher = (row =~ pattern)

                        rolesToPoliciesObjs << new rolesToPoliciesObj(environment: matcher[0][1], policyNames: matcher[1][1], policyARNs: "", roleName: matcher[2][1])

                        
                    }

                    // rolesToPoliciesObjs.each { obj ->
                    //     echo "${obj.environment} ${obj.policyNames} ${obj.roleName}"
                    // }
                }
            }
        }
        // stage('GetEnvironmentDetails') {
        //     steps {
        //         script {
        //             // environment = params.Environment

        //             def rolesByEnvironment = rolesToPoliciesObjs.groupBy { it.environment }
                    
        //             rolesByEnvironment.each { environment, rolesToPoliciesObj ->
        //                 echo "${environment}"
        //                 echo "${rolesToPoliciesObj}"
        //             }
        //             // switch (environment) {
        //             //     case 'rod_aws':
        //             //         credentialsId = 'rod_aws'
        //             //         break
        //             //     default:
        //             //         error("No matching environment details found that matches \"${environment}\".")
        //             // }

        //             // echo "Successfully retrieved environment details for environment \"${environment}\"."          
        //         }
        //     }
        // }
        stage('GetPolicyARNs') {
            steps {
                script {
                    // policyNames = params.PolicyNames

                    // echo "${policyNames}"

                    def rolesByEnvironment = rolesToPoliciesObjs.groupBy { it.environment }
                    
                    rolesByEnvironment.each { environment, objs ->
                        
                        echo "${environment}"

                        def awsCredential = ""

                        // if(environment=="Deltekdev"){
                        //     awsCredential = 'infra-at-dev'
                        // }
                        if(environment=="dcoflexplus"){
                            awsCredential = 'infra-at-flexplus'
                        }
                        // else if(environment=="Costpoint"){
                        //     awsCredential = 'infra-at-costpoint'
                        // }
                        // else if(environment=="DCO"){
                        //     awsCredential = 'infra-at-dco'
                        // }
                        // else if(environment=="Offsec"){
                        //     awsCredential = 'infra-at-offsec'
                        // }
                        // else if(environment=="GovwinProduction"){
                        //     awsCredential = 'infra-at-govwinpd'
                        // }
                        // else if(environment=="GovwinDev"){
                        //     awsCredential = 'infra-at-govwindv'
                        // }
                        // else if(environment=="Interspec"){
                        //     awsCredential = 'infra-at-interspec'
                        // }
                        // else if(environment=="Especs"){
                        //     awsCredential = 'infra-at-especs'
                        // }
                        // else if(environment=="Arcom"){
                        //     awsCredential = 'infra-at-arcom'
                        // }
                        // else if(environment=="DeltekEA"){
                        //     awsCredential = 'infra-at-deltekea'
                        // }
                        // else if(environment=="Onvia"){
                        //     awsCredential = 'infra-at-onvia'
                        // }
                        // else if(environment=="GlobalOSS"){
                        //     awsCredential = 'infra-at-oss'
                        // }
                        // else if(environment=="ECMaconomy"){
                        //     awsCredential = 'infra-at-ecmaconomy'
                        // }
                        // else if(environment=="SecuritySandbox"){
                        //     awsCredential = 'infra-at-secsandbox'
                        // }
                        // else if(environment=="DeliverySandbox"){
                        //     awsCredential = 'infra-at-delsandbox'
                        // }
                        // else if(environment=="Unionpoint"){
                        //     awsCredential = 'infra-at-unionpoint'
                        // }
                        // else if(environment=="ServiceBroker"){
                        //     awsCredential = 'infra-at-servicebroker'
                        // }
                        // else if(environment=="Archsandbox"){
                        //     awsCredential = 'infra-at-archsandbox'
                        // }
                        // else if(environment=="SC-Vantagepoint"){
                        //     awsCredential = 'infra-at-sc-vantagepoint'
                        // }
                        // else if(environment=="EC-MGT"){
                        //     awsCredential = 'infra-at-ec-mgt'
                        // }
                        // else if(environment=="PieterEerlings"){
                        //     awsCredential = 'infra-at-pieter-eerlings'
                        // }
                        // else if(environment=="sc-dhtmlx"){
                        //     awsCredential = 'infra-at-sc-dhtmlx'
                        // }
                        // else if(environment=="sc-ssec"){
                        //     awsCredential = 'infra-at-sc-ssec'
                        // }
                        // else if(environment=="ec-ssec"){
                        //     awsCredential = 'infra-at-ec-ssec'
                        // }

                        withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',credentialsId: "${awsCredential}", accessKeyVariable: 'AWS_ACCESS_KEY_ID', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
                            
                            def policyNamesGroup = objs.collect { it.policyNames }
                                
                            policyNamesGroup.each { policyNames ->
                                // echo "${policyNames}"

                                def cmd = "python3 1_get_policy_arns.py '${policyNames}'"

                                // Executes the AWS CLI command and does some post-processing.
                                policyARNs = sh(script: cmd, returnStdout: true).trim()

                                echo "${policyARNs}"
                                
                                rolesToPoliciesObjs.find { it.policyNames == policyNames && it.environment == environment }?.policyARNs = policyARNs

                                // echo "${policyARNs}"
                                //sleep(30)
                            }
                        }
                    }

                    // rolesToPoliciesObjs.each { obj ->
                    //     def str = "\n"
                    //     str += "Environment: ${obj.environment}\n"
                    //     str += "Role: ${obj.roleName}\n"
                    //     str += "Policy Names: ${obj.policyNames}\n"
                    //     str += "Policy ARNs: ${obj.policyARNs}\n"
                    
                    //     echo "${str}"
                    // }
                }
            }
        }
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

