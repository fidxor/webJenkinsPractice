pipeline {
    agent any

    stages {
        stage("Checkout") {
			steps {
				checkout scm
			}
		}
        stage("build") {
            steps {
                sh 'docker build -t fidxor/pythonweb:0.2 .'
            }
        }
        stage("deploy") {
            steps {
                sh 'docker push fidxor/pythonweb:0.2'
            }
        }
    }
}