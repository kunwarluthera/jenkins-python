pipeline {
    agent none
    stages {
        stage('Build') {
            agent { dockerfile {
                args '-p 5000:5000'
            } }
            steps {
                sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
            }
        }
        stage('Test') { 
            agent { dockerfile {
                args '-p 5000:5000'
            }}
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

        