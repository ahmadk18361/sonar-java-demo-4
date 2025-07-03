pipeline {
    agent any

    tools {
        maven 'Maven'
        
    }

    environment {
        SONARQUBE_SERVER = 'SonarQube' // Must match Jenkins config name exactly
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/ahmadk18361/sonar-java-demo.git'
            }
        }

        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }

        stage('SonarQube Scan') {
            steps {
                withSonarQubeEnv("${SONARQUBE_SERVER}") {
                    withCredentials([string(credentialsId: 'SONAR_TOKEN', variable: 'SONAR_TOKEN')]) {
                        bat """
                            mvn sonar:sonar ^
                              -Dsonar.projectKey=ahmadk18361_sonar-java-demo ^
                              -Dsonar.organization=ahmadk18361 ^
                              -Dsonar.host.url=https://localhost9000 ^
                              -Dsonae.login=%SONAR_TOKEN%
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
