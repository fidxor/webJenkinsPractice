pipeline {
    environment {
        REPOSITORY = "fidxor/pythonweb"
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-fidxor')
        GIT_TOKEN = credentials('git-fidxor') // Git 토큰 자격 증명 ID로 교체하세요
        TARGET_REPO_URL = 'github.com/fidxor/argocdJenkinsPractice.git'
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
            stage("Commit and Push to Another Repo") {
                steps {
                    script {
                        dir('target-repo') {
                            withCredentials([usernamePassword(credentialsId: 'git-fidxor', passwordVariable: 'gitPassword', usernameVariable: 'gitUsername')]) {
                                sh 'git config --global user.name "fidxor"' // 사용자 이름 설정
                                sh 'git config --global user.email "fidxordl5404@gmail.com"' // 사용자 이메일 설정
                                // target-repo 디렉토리가 이미 존재하는지 확인하고, 존재하면 삭제
                                sh '''
                                    if [ -d target-repo ]; then
                                        rm -rf target-repo
                                    fi
                                '''

                                sh 'git clone https://$TARGET_REPO_URL target-repo'

                                sh "sed -i 's|image: fidxor/pythonweb:[^ ]*|image: fidxor/pythonweb:$BUILD_NUMBER|' target-repo/pythonweb/deployment.yml"

                                sh 'git add .'
                                sh 'git commit -m "update deployment image version $BUILD_NUMBER"'
                                sh 'git push https://${gitUsername}:${gitPassword}@$TARGET_REPO_URL'                                                    
                            }
                        }                        
                        // // 환경 설정
                        // sh 'git config --global user.name "fidxor"' // 사용자 이름 설정
                        // sh 'git config --global user.email "fidxordl5404@gmail.com"' // 사용자 이메일 설정

                        // // target-repo 디렉토리가 이미 존재하는지 확인하고, 존재하면 삭제
                        // sh '''
                        //     if [ -d target-repo ]; then
                        //         rm -rf target-repo
                        //     fi
                        // '''

                        // // 타겟 저장소 클론
                        // sh 'git clone https://$TARGET_REPO_URL target-repo'

                        // // 파일 변경 및 커밋
                        // sh "sed -i 's|image: fidxor/pythonweb:[^ ]*|image: fidxor/pythonweb:$BUILD_NUMBER|' target-repo/pythonweb/deployment.yml"
                        // dir('target-repo') {
                        //     sh 'git add .'
                        //     sh 'git commit -m "update deployment image version $BUILD_NUMBER"'
                        //     sh 'git push origin main'
                        // }
                    }
                }
            }
            stage("cleaning up") {
                steps {
                    sh 'docker rmi $REPOSITORY:$BUILD_NUMBER'
                }
            }            
        }
        post {
            always {
                emailext body: 'A Test EMail', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], subject: 'Test'
            }
        }
}

