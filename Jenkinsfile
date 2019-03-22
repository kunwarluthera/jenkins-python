pipeline {
    agent none
    stages {
        stage('Build') {
            agent { dockerfile {
                args '-p 5000:5000'
            } }
            environment {
        AWS_ACCESS_KEY_ID     = credentials('jenkins-aws-secret-key-id')
        AWS_SECRET_ACCESS_KEY = credentials('jenkins-aws-secret-access-key')
         REDIS_HOST     = credentials('REDIS_HOST')
        REDIS_PORT = credentials('REDIS_PORT')
    }
            steps {
                sh 'python  app.py'
            }
        }
    }
}

        