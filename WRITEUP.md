# Write-up Template

## Analyze, choose, and justify the appropriate resource option for deploying the app.

From a cost perspective, Azure Web Apps are generally more affordable for typical web applications. Pricing is based on App Service Plans (such as Basic, Standard, or Premium), where you pay for the compute resources allocated to your app regardless of the actual usage. For example, a Standard S1 plan might cost around $74 USD per month per instance. Since the infrastructure is shared and managed by Azure, there are no separate charges for OS licensing, patching, or storage (outside of file storage or backups). Auto-scaling is included in most plans, and you only pay for additional instances when scaling out. Azure VMs, on the other hand, involve more granular pricing. You are billed per hour for the VM’s compute size (e.g., Standard B2s, D2s_v3), along with associated costs for the operating system (if using Windows), managed disks, backup, bandwidth, and any other add-on services. Even when a VM is idle, it incurs charges unless it is explicitly deallocated. This can lead to higher total costs, especially when running multiple services on the same VM or when high availability needs require multiple VM instances. While VMs offer greater flexibility—such as installing any required software, using custom images, or running non-web workloads—they also come with higher administrative overhead and ongoing maintenance responsibility.

In terms of scalability, Azure Web App clearly has the advantage for most web workloads. It includes built-in auto-scaling features that can respond to changes in CPU usage, memory utilization, or scheduled patterns. Scaling horizontally (adding more instances) or vertically (increasing compute size) is straightforward through the Azure portal. The App Service also comes with integrated load balancing, high availability features, and the ability to deploy across multiple regions with minimal effort. Conversely, Azure VMs require more manual configuration to scale. While Azure provides tools like Virtual Machine Scale Sets and Load Balancers, these must be explicitly set up and maintained. Horizontal scaling involves creating and managing multiple VMs, and vertical scaling may require resizing the VM, which could involve downtime. Moreover, achieving redundancy and availability requires setting up availability sets or availability zones, which adds complexity and cost.

In summary, Azure Web App is the better choice if you want a cost-effective, scalable, and low-maintenance solution for hosting web applications, REST APIs, or lightweight backend services. It’s ideal for teams looking to focus on application development rather than infrastructure management. Azure VMs are more suited for scenarios that require custom OS configurations, legacy software environments, or non-web workloads that don’t fit within the constraints of a managed platform. However, this flexibility comes at the cost of higher complexity, increased administrative effort, and potentially higher long-term expenses.


### Assess app changes that would change your decision.

- Need Full Control Over the Operating System
- Need Custom Security or Networking Setup
- Need Persistent Local Storage or System-Level File Access
- Hosting Multiple Services on One Machine
