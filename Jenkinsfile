pipeline {
    environment {
        REPOSITORY = "fidxor/pythonweb"
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-fidxor')
        dockerImage = ''
    }

    agent any

        stages {
            stage("Checkout") {
                steps {
                    checkout scm
                }
            }
            stage("build") {
                steps {
                    sh 'docker build -t $REPOSITORY:$BUILD_NUMBER .'

                }
            }
            stage("login") {
                steps {
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                }
            }
            stage("deploy") {
                steps {
                    sh 'docker push $REPOSITORY:$BUILD_NUMBER'
                }
            }
            stage("cleaning up") {
                steps {
                    sh 'docker rmi $REPOSITORY:$BUILD_NUMBER'
                }
            }
            post {
                always {
                    emailext body: 'A Test EMail', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], subject: 'Test'
                }
            }
        }
}

