pipeline {
    agent any

    tools {
        maven 'Maven'
        jdk 'jdk-17'
    }

    environment {
        SONARQUBE_SERVER = 'Sonar-cve's' // Must match Jenkins config name exactly
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/ahmadk18361/sonar-java-demo-4.git'
            }
        }
    }
        
        stage('Remediate Vulnerabilities') {
            steps {
                bat 'remediation_cve_2021_33813.py src/main/java/com/example/CommonsIOCVE2021_33813Example.java'
                bat 'remediation_cve_2021_33813.py src/main/java/com/example/SecretLoggingBufferedInputExample.java'
                bat 'remediation_cve_2021_33813.py src/main/java/com/example/SecretLoggingCmdArgsExample.java'

            }
        }
        
         stage ('Debug Sonar Token') {
                steps {
                    withCredentials([string(credentialsId: '2ndsonar', variable: 'SONAR_TOKEN')]) {
                        bat 'echo Debug: token is %SONAR_TOKEN%'
                    }
                }
            }

        
        stage('SonarQube Scan') {
            steps {
                withSonarQubeEnv("${Sonar-cve-s}") {
                    withCredentials([string(credentialsId: '2ndsonar', variable: 'SONAR_TOKEN')]) {
                        bat 'mvn sonar:sonar -Dsonar.token=$SONAR_TOKEN'
                        bat 'echo Sonar token: %SONAR_TOKEN'
                       bat """
                            mvn clean verify sonar:sonar \
                              -Dsonar.projectKey=sonar-cve-fix3 \
                              -Dsonar.projectName='sonar-cve-fix3' \
                              -Dsonar.host.url=http://localhost:9000 \
                              -Dsonar.sources=src/main/java/com/example
                              -Dsonar.token=sqp_48e700452be9b7e45e8935b54de4d8bd3d271eb2
                            """
                    }
                }
            }
        }
    }
