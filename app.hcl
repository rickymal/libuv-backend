# Application configuration

app "myapp" {
  name        = "My Complex Application"
  description = "A sophisticated application with various components"
  version     = "1.2.3"

  metadata {
    environment = "production"
    team        = "backend"
    cost_center = "CC123"
  }

  build {
    dockerfile = "Dockerfile"
    context    = "."
    args = {
      GO_VERSION = "1.17"
      NODE_VERSION = "14"
    }
    target = "production"
  }

  deploy {
    type = "kubernetes"
    
    kubernetes {
      namespace = "myapp-prod"
      replicas  = 3
      
      resources {
        cpu    = "500m"
        memory = "512Mi"
      }
      
      readiness_probe {
        http_get {
          path = "/healthz"
          port = 8080
        }
        initial_delay_seconds = 10
        period_seconds        = 5
      }
    }
  }

  network {
    port {
      local  = 8080
      remote = 80
      public = true
    }
    
    domain {
      name = "myapp.example.com"
      ssl  = true
    }
  }

  database "main" {
    type     = "postgresql"
    version  = "13"
    name     = "myapp_production"
    username = "myapp_user"
    password = env("DB_PASSWORD")
  }

  cache "redis" {
    type    = "redis"
    version = "6.2"
  }

  environment {
    LOG_LEVEL   = "info"
    API_KEY     = env("API_KEY")
    ENVIRONMENT = "production"
  }

  dependencies {
    service "auth" {
      image = "auth-service:v1.0"
    }
    service "analytics" {
      image = "analytics-service:v2.1"
    }
  }

  observability {
    logging {
      driver = "fluentd"
      options = {
        fluentd-address = "localhost:24224"
      }
    }
    
    metrics {
      provider = "prometheus"
      path     = "/metrics"
    }
    
    tracing {
      provider = "jaeger"
      endpoint = "http://jaeger-collector:14268/api/traces"
    }
  }

  scaling {
    auto = true
    min  = 2
    max  = 10
    
    metrics {
      type      = "cpu"
      threshold = 75
    }
  }

  lifecycle {
    pre_start    = ["./scripts/pre-start.sh"]
    post_start   = ["./scripts/post-start.sh"]
    pre_stop     = ["./scripts/pre-stop.sh"]
    post_stop    = ["./scripts/post-stop.sh"]
    health_check = "/healthz"
  }
}
