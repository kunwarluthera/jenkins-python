pipeline {
    agent none
    stages {
        stage('Build') {
            agent { dockerfile {
                filename 'Dockerfile'
                dir '/var/jenkins_home/workspace/simple-python-pyinstaller-app/'
                label 'kunwarluthera/simple-python-py'
                additionalBuildArgs  '--build-arg version=1.0.2'
                args '-d kunwarluthera/simple-python-py python app.py -- --coverage'
            } }
            steps {
                sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
            }
        }
        stage('Test') { 
            steps {
                sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py' 
            }
            post {
                always {
                    junit 'test-reports/results.xml' 
                }
            }
        }
    }
}

        