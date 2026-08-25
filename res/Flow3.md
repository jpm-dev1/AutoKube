# ☸️ K8sWhisperer Architecture & Pipeline Flow

This document details the internal working process of the K8sWhisperer autonomous SRE agent. The system operates on a deterministic 6-node state graph designed to ensure zero data leakage and strict operational safety.

## 📊 Visual Flowchart


```mermaid
flowchart TD
    %% Define Node Styling
    classDef trigger fill:#f9f9f9,stroke:#333,stroke-width:2px,stroke-dasharray: 5 5
    classDef k8s fill:#326ce5,stroke:#fff,stroke-width:2px,color:#fff
    classDef ai fill:#f4a261,stroke:#333,stroke-width:2px,color:#000
    classDef manual fill:#e76f51,stroke:#fff,stroke-width:2px,color:#fff
    classDef execute fill:#2a9d8f,stroke:#fff,stroke-width:2px,color:#fff
    classDef blockchain fill:#264653,stroke:#fff,stroke-width:2px,color:#fff

    %% Trigger/Loop
    Timer(((Continuous 30s<br/>Polling Loop))):::trigger --> Node1

    %% External Systems Subgraphs
    subgraph K8sCluster [Kubernetes Cluster]
        API[(Kube-API)]:::k8s
    end

    subgraph AI_Engine [Air-Gapped AI Engine]
        Ollama[(Local Ollama<br/>Llama 3.2 3B)]:::ai
    end
    
    subgraph Blockchain [Audit & Compliance]
        Stellar[(Stellar Testnet<br/>Ledger)]:::blockchain
    end

    %% Pipeline Nodes
    subgraph Pipeline [The 6-Node State Graph]
        direction TB
        Node1[1. OBSERVE<br/>Fetch Pods & Events]
        Node2{2. DETECT<br/>Is there a failure?}
        Node3[3. DIAGNOSE<br/>Extract container logs]
        Node4[4. PLAN<br/>Draft JSON Remediation]
        Gate{SAFETY GATE<br/>SRE Approval?}:::manual
        Node5[5. EXECUTE<br/>Apply Patch/Restart]:::execute
        Node6[6. EXPLAIN<br/>Write Audit Log]
    end

    %% Flow Logic
    API <-.-> Node1
    Node1 --> Node2
    Node2 -- "No (Cluster Healthy)" --> Timer
    Node2 -- "Yes (e.g., CrashLoop)" --> Node3
    
    Node3 -. "Send Logs" .-> Ollama
    Ollama -. "Return Root Cause" .-> Node3
    
    Node3 --> Node4
    Node4 -. "Request Plan" .-> Ollama
    Ollama -. "Return JSON Plan" .-> Node4
    
    Node4 --> Gate
    
    Gate -- "Approved" --> Node5
    Gate -- "Denied / Edited" --> Node6
    
    Node5 -- "kubectl apply/delete" --> API
    Node5 --> Node6
    
    Node6 -- "Anchor SHA-256 Hash" --> Stellar
