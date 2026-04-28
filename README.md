# ThermaKube

ThermaKube is a cloud-native scientific orchestrator that simulates 2D Heat Diffusion across a distributed Kubernetes cluster. It demonstrates the transition from local scientific scripts to scalable, self-healing infrastructure.

##  The Science
The core solver implements the **2D Heat Equation** using the Finite Difference Method:

$$\frac{\partial u}{\partial t} = \alpha \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} \right)$$

Where:
- $u$ is the temperature field.
- $\alpha$ is the thermal diffusivity.
- The simulation uses a vectorised stencil operation for performance.

##  Technical Architecture
- **Orchestration:** Kubernetes (k3d) managing multiple solver replicas.
- **Containerisation:** Docker with optimised lightweight Python images.
- **CI/CD:** GitHub Actions for automated linting (Ruff) and validation.
- **Language:** Python 3.11 with NumPy.

##  Getting Started
To run this project locally without cloud fees:

1. **Clone the repo:**

   ```bash
   cd thermakube
```

2. **Run the automated setup:**
Ensure Docker is running, then execute:
```bash
  chmod +x reset_cluster.sh
  ./reset_cluster.sh
```

3. **Observe the simulation:**
```bash
  kubectl get pods
  kubectl logs -l app=heat-solver --tail=20
```

## DevOps Features
. Self-Healing: If a solver pod fails, Kubernetes automatically restarts it to maintain the simulation state.
. Resource Constraints: Pods are limited to 512MiB RAM to ensure cluster stability.
 
. Declarative Infrastructure: All configurations are managed via YAML manifests.

