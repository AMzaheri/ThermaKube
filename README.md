![CI Status](https://github.com/AMzaheri/ThermaKube/actions/workflows/ci.yml/badge.svg)

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

And 
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
- Self-Healing: If a solver pod fails, Kubernetes automatically restarts it to maintain the simulation stat.
- Resource Constraints: Pods are limited to 512MiB RAM to ensure cluster stability.
- Declarative Infrastructure: All configurations are managed via YAML manifests.

##  Scalability
In a research environment, we might need to run hundreds of simultaneous simulations with different boundary conditions. Kubernetes makes this trivial to manage

### 1. Scaling the Simulation
To scale the number of active heat solvers from 3 to 10 instances, while the cluster is running run the following command:
```bash
  ./reset_cluster.sh
```
Once the pods are listed as Running under `kubectl get pods`, we can proceed with the experiments, run
```bash
  kubectl scale deployment heat-solver-deployment --replicas=10
```
Run `kubectl get pods`. We’ll see 10 pods working together. 

When we're done, we'll bring it back to a manageable number:
```bash
  kubectl scale deployment heat-solver-deployment --replicas=3
```
### 2. Self-Healing Infrastructure
If a pod crashes due to a memory limit or a node failure, the Kubernetes ReplicaSet will automatically detect the failure and spin up a new instance to maintain the desired state.

Manually delete one of the running pods and watch how quickly the cluster heals itself:
```bash
  # Delete a specific pod
  kubectl delete pod <pod-name>

  # Immediately check the status to see a new pod being created
  kubectl get pods
```

