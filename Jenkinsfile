pipeline {
    agent none
    stages {
        stage('Build') {
            agent { dockerfile true }
            steps {
                sh 'docker build -t kunwarluthera/simple-python-py .'
            }
        }
        stage('Test') { 
            agent { dockerfile true }
            steps {
                sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py' 
                sh 'docker run -d kunwarluthera/simple-python-py python app.py -- --coverage'
            }
            post {
                always {
                    junit 'test-reports/results.xml' 
                }
            }
        }
    }
}