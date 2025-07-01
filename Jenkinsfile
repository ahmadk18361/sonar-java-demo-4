pipeline {
    agent any

    tools {
        maven 'Maven'        // Make sure this matches what you named Maven under Jenkins tools
        sonarQubeScanner ' SonarQube' 
        jdk 'jdk-17'         // Or whatever JDK name you configured in Jenkins
    }

    environment {
        SONARQUBE_SERVER = 'SonarCloud'  // Must match exactly the SonarQube name you set in Jenkins
        SONAR_PROJECT_KEY = 'sonar-java-analysis'
        SONAR_TOKEN = credentials ('e8635ada11a2493b8127512f2fc5ce2f') //
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/ahmadk18361/sonar-java-demo.git'
            }
        }

        stage('Build') {
            steps {
                dir('sonarJavaDemo') {
                    sh 'mvn clean package'
                }
            }
        }

         stage('SonarQube Scan') {
            steps {
                dir('SonarJavaDemo') {
                    withSonarQubeEnv("${SONARQUBE_SERVER}") {
                        sh "mvn sonar:sonar"
                    }
                }
            }
        }
    }
}       
