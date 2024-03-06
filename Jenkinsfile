class rolesToPoliciesObj {
    String environment
    String policyNames
    String policyARNs
    String roleName
}

String getAwsCredential(String environment) {
    switch (environment) {
        case "Deltekdev":
            return 'infra-at-dev'
        case "dcoflexplus":
            return 'infra-at-flexplus'
        case "Costpoint":
            return 'infra-at-costpoint'
        case "DCO":
            return 'infra-at-dco'
        case "Offsec":
            return 'infra-at-offsec'
        case "GovwinProduction":
            return 'infra-at-govwinpd'
        case "GovwinDev":
            return 'infra-at-govwindv'
        case "Interspec":
            return 'infra-at-interspec'
        case "Especs":
            return 'infra-at-especs'
        case "Arcom":
            return 'infra-at-arcom'
        case "DeltekEA":
            return 'infra-at-deltekea'
        case "Onvia":
            return 'infra-at-onvia'
        case "GlobalOSS":
            return 'infra-at-oss'
        case "ECMaconomy":
            return 'infra-at-ecmaconomy'
        case "SecuritySandbox":
            return 'infra-at-secsandbox'
        case "DeliverySandbox":
            return 'infra-at-delsandbox'
        case "Unionpoint":
            return 'infra-at-unionpoint'
        case "ServiceBroker":
            return 'infra-at-servicebroker'
        case "Archsandbox":
            return 'infra-at-archsandbox'
        case "SC-Vantagepoint":
            return 'infra-at-sc-vantagepoint'
        case "EC-MGT":
            return 'infra-at-ec-mgt'
        case "PieterEerlings":
            return 'infra-at-pieter-eerlings'
        case "sc-dhtmlx":
            return 'infra-at-sc-dhtmlx'
        case "sc-ssec":
            return 'infra-at-sc-ssec'
        case "ec-ssec":
            return 'infra-at-ec-ssec'
        default:
            return 'default-credential' // or null if you prefer
    }
}


def rolesToPoliciesObjs = []

pipeline {

  agent { label 'jenkins-slave-linux-cu01use1gs1jx01' }
  
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
        stage('GetPolicyARNs') {
            steps {
                script {
                    // policyNames = params.PolicyNames

                    // echo "${policyNames}"

                    def rolesByEnvironment = rolesToPoliciesObjs.groupBy { it.environment }
                    
                    rolesByEnvironment.each { environment, objs ->
                        
                        echo "${environment}"

                        def awsCredential = getAwsCredential(environment)

                        withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',credentialsId: "${awsCredential}", accessKeyVariable: 'AWS_ACCESS_KEY_ID', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {

                            objs.each { obj ->

                                def roleName = obj.roleName
                                def policyNames = obj.policyNames

                                def cmd = "python3 1_get_policy_arns.py '${policyNames}'"

                                // Executes the AWS CLI command and does some post-processing.
                                policyARNs = sh(script: cmd, returnStdout: true).trim()
                                
                                rolesToPoliciesObjs.find { (it.policyNames == policyNames && it.environment == environment) && it.roleName == roleName }?.policyARNs = policyARNs
                            }
                        }
                    }

                    rolesToPoliciesObjs.each { obj ->
                        def str = "\n"
                        str += "Environment: ${obj.environment}\n"
                        str += "Role: ${obj.roleName}\n"
                        str += "Policy Names: ${obj.policyNames}\n"
                        str += "Policy ARNs: ${obj.policyARNs}\n"
                    
                        echo "${str}"
                    }
                }
            }
        }
        stage('CreateRole') {
            steps {
                script {
                    // policyNames = params.PolicyNames

                    // echo "${policyNames}"

                    def rolesByEnvironment = rolesToPoliciesObjs.groupBy { it.environment }
                    
                    rolesByEnvironment.each { environment, objs ->
                        
                        echo "${environment}"

                        def awsCredential = getAwsCredential(environment)

                        withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',credentialsId: "${awsCredential}", accessKeyVariable: 'AWS_ACCESS_KEY_ID', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {

                            objs.each { obj ->

                                def roleName = obj.roleName

                                def cmd = "python3 2_create_role.py '${roleName}'"

                                // Executes the AWS CLI command and does some post-processing.
                                def newRole = sh(script: cmd, returnStdout: true).trim()
                                echo "${newRole}"
                            }
                        }
                    }
                }
            }
        }
        stage('AttachPoliciesToRoles') {
            steps {
                                script {
                    // policyNames = params.PolicyNames

                    // echo "${policyNames}"

                    def rolesByEnvironment = rolesToPoliciesObjs.groupBy { it.environment }
                    
                    rolesByEnvironment.each { environment, objs ->
                        
                        echo "${environment}"

                        def awsCredential = getAwsCredential(environment)

                        withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',credentialsId: "${awsCredential}", accessKeyVariable: 'AWS_ACCESS_KEY_ID', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {

                            objs.each { obj ->

                                def roleName = obj.roleName
                                def policyARNs = obj.policyARNs

                                def cmd = "python3 3_attach_policies_to_role.py '${roleName}' '${policyARNs}'"

                                // Executes the AWS CLI command and does some post-processing.
                                def policyAttachmentResponse = sh(script: cmd, returnStdout: true).trim()
                                echo "${policyAttachmentResponse}"
                            }
                        }
                    }
                }
            }
        }
    }
}

