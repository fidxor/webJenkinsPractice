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
                    sh 'docker build -t fidxor/pythonweb:$BUILD_NUMBER .'

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
        }
}

// pipeline {
//     agent any

//     environment {
//         REPOSITORY = "fidxor/pythonweb"
//         DOCKERHUB_CREDENTIALS = credentials('fidxor')
//         dockerImage = ''
//     }

//     stages {
//         stage("Checkout") {
// 			steps {
// 				checkout scm
// 			}
// 		}
//         stage("build") {
//             steps {
//                 sh 'docker build -t fidxor/pythonweb:$BUILD_NUMBER .'

//             }
//         }
//         stage("login") {
//             steps {
//                 sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
//             }
//         }
//         stage("deploy") {
//             steps {
//                 sh 'docker push $REPOSITORY:$BUILD_NUMBER'
//             }
//         }
//     }
// }