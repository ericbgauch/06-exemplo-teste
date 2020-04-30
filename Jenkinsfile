pipeline {
    agent any
    post {
        always {
            cleanWs()
        }
    }
    stages{
        stage("Test") {
            steps {
                sh 'python3 -m unittest tests.py'
            }
        }
        stage("Build and Deploy Staging") {
            when { branch 'master' }
            stages {
                stage("Package") {
                    steps {
                        script {
                            echo 'Packaging'
                        }
                    }
                }
                stage("Build and push image") {
                    steps {
                        echo 'Building and pushing image'
                    }
                }
                stage("Deploy Staging") {
                    stages {
                        stage("Pull latest image") {
                            steps {
                                echo 'Pulling image'
                            }
                        }
                        stage("Recriate service") {
                            steps {
                                echo 'Recriating image'
                            }
                        }
                    }
                }
            }
        }
        stage("Deploy Production") {
            when { buildingTag() }
            stages {
                stage("Pull latest image") {
                    steps {
                        echo 'Pulling image'
                    }
                }
                stage("Recriate service") {
                    steps {
                        echo 'Recriating service'
                    }
                }
            }
        }
    }
}
