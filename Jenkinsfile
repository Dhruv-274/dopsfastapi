pipeline {
    agent any
    environment {
        dockerCred = credentials('dockerhub-credentials')
        dockerImg = "dhruvrs/dockapp"
    }
    stages {
        stage('Clone Repo') {
            steps {
                git(
                    url: 'https://github.com/Dhruv-274/dopsfastapi.git',
                    credentialsId: 'github-credentials',
                    branch: 'main'
                )
            }
        }
        stage('Build Image') {
            steps {
                script {
                    docker.build(dockerImg)
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', dockerCred) {
                        docker.image(dockerImg).push()
                    }
                }
            }
        }
    }
}
