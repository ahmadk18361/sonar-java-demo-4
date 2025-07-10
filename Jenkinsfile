pipeline {
    agent any

    tools {
        maven 'Maven'
        jdk 'jdk-17'
    }

    environment {
        SONARQUBE_SERVER = 'SonarCloud' // Must match Jenkins config name exactly
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/ahmadk18361/sonar-java-demo.git'
            }
        }

        stage('Build') {
            steps {
                bat 'mvn clean package'
            }
        }

        stage('SonarQube Scan') {
            steps {
                withSonarQubeEnv("${SONARQUBE_SERVER}") {
                    withCredentials([string(credentialsId: 'SONAR_TOKEN', variable: 'SONAR_TOKEN')]) {
                        sh """
                           mvn clean verify sonar:sonar \
                            -Dsonar.projectKey=SonarJavaDemo \
                            -Dsonar.projectName='SonarJavaDemo' \
                            -Dsonar.host.url=http://localhost:9000 \
                            -Dsonar.token=sqp_81fe24b794f8ec9d9bc95b1f8baf1eab49cdcf2f
                        """
                    }
                }
            }
        }
        stage('SonarQube Analysis') {
            steps {
                wihSonarQubeEnv ('YourSonarServer') {
                    sh 'mvn clean verfiy sonar:sonar -Dsonar.projectkey=your-project-key -Dsonar.login=your-token'
                }
            }
        }
        stage('Security Scan - SpotBugs') {
            steps { 
                sh 'mvn verify spotbugs:check'

            }
        }

    }
}
