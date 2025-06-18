pipeline{
    agent any
    environment{
        dockerCred=credentials('dockerhub-credentials')
        dockerImg="dhruvrs/baseapp:latest"
    }
    stage('git'){
        steps{
            git (
                url:'https://github.com/Dhruv-274/dopsfastapi.git',
                credentialsId:'github-credentials',
                branch:'main'
            )
        }
    }
    stage('build'){
        steps{
            script{
                docker.build(dockerImg)
            }

        }
    }
    stage('push'){
        steps{
           script{
             docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials'){
                docker.image('dockerImg').push('latest')
            }
           }
        }
    }
}