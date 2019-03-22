pipeline {
    agent none
    stages {
        stage('Build') {
            agent { dockerfile true }
            steps {
                sh 'python -m py_compile sources/add2vals.py sources/calc.py'
            }
        }
        stage('Test') { 
            agent { dockerfile true }
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