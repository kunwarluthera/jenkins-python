pipeline {
  environment {
    registry = "kunwarluthera/jenkins-docker"
    registryCredential = 'dockerhub'
  }
  agent any
  stages {
    stage('Building image') {
        agent { dockerfile true}
      steps{
        script {
          docker.build registry + ":$BUILD_NUMBER"
        }
      }
    }
  }
}      