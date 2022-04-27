pipeline{
    agent any

    environment{
        NEW_VERSION = '1.3.0'
    }

    stages{
        stage("build"){
            when{
                expression{
                    
                }
            }
            steps{
                echo "building version ${NEW_VERSION}..."
            }
            post{
                always{
                    echo "========always========"
                }
                success{
                    echo "========A executed successfully========"
                }
                failure{
                    echo "========A execution failed========"
                }
            }
        }
    }
    post{
        always{
            echo "========always========"
        }
        success{
            
            echo "========pipeline executed successfully ========"
        }
        failure{
            echo "========pipeline execution failed========"
        }
    }
}