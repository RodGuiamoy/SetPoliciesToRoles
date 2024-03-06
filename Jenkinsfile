class rolesToPoliciesObj {
    String environment
    String policyNames
    String policyARNs
    String roleName
}

String getAwsCredential(String environment) {
    switch (environment) {
        case "Avitru":
            return 'infra-at-arcom'
        case "dcoflexplus":
            return 'infra-at-flexplus'
        case "dcosandbox":
            return 'infra-at-delsandbox'
        case "DeltekCostPoint":
            return 'infra-at-costpoint'
        case "DeltekDCO":
            return 'infra-at-dco'
        case "DeltekDCODev":
            return 'infra-at-dev'
        case "EC-Maconomy-Sandbox":
            return 'infra-at-ecmaconomy'
        case "EC-SSEC":
            return 'infra-at-ec-ssec'
        case "GlobalOSS":
            return 'infra-at-oss'
        case "GovWin":
            return 'infra-at-govwinpd'
        case "GovWinDev":
            return 'infra-at-govwindv'
        case "OnviaInc":
            return 'infra-at-onvia'
        case "SC-Cloud-Arch-Sandbox":
            return 'infra-at-archsandbox'
        case "SC-DHTMLX":
            return 'infra-at-sc-dhtmlx'
        case "SC-SSEC":
            return 'infra-at-sc-ssec'
        case "Unionpoint":
            return 'infra-at-unionpoint'
        default:
            return '' 
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

                        try {
                            withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',credentialsId: "${awsCredential}", accessKeyVariable: 'AWS_ACCESS_KEY_ID', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {

                                objs.each { obj ->

                                    def roleName = obj.roleName
                                    def policyARNs = obj.policyARNs

                                    def cmd = "python3 3_attach_policies_to_role.py '${roleName}' '${policyARNs}'"

                                    try {
                                        // Executes the AWS CLI command and does some post-processing.
                                        def policyAttachmentResponse = sh(script: cmd, returnStdout: true).trim()
                                        echo "${policyAttachmentResponse}"
                                    }
                                    catch (Exception e) {
                                    unstable("An error occurred: ${e.message}")
                                    }
                                }
                            }
                        }
                        catch (Exception e) {
                            unstable("An error occurred: ${e.message}")
                        }

                        
                    }
                }
            }
        }
    }
}

