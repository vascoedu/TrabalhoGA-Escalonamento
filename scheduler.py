import random

class Worker:
    def __init__(self, nome, cpu, memoria, disco, latencia):
        self.nome = nome
        self.cpu = cpu
        self.memoria = memoria
        self.disco = disco
        self.latencia = latencia
        self.pods = []

    def pode_alocar(self, pod):
        return (self.cpu >= pod.cpu and 
                self.memoria >= pod.memoria and
                self.disco >= pod.disco)

    def alocar(self, pod):
        self.cpu -= pod.cpu
        self.memoria -= pod.memoria
        self.disco -= pod.disco
        self.pods.append(pod)

class Pod:
    def __init__(self, nome, cpu, memoria, disco):
        self.nome = nome
        self.cpu = cpu
        self.memoria = memoria
        self.disco = disco

def calcular_score(worker):
    peso_cpu = 0.4
    peso_mem = 0.3
    peso_disco = 0.2
    peso_lat = 0.1

    return (peso_cpu * worker.cpu +
            peso_mem * worker.memoria +
            peso_disco * worker.disco -
            peso_lat * worker.latencia)

def escalonar(pods, workers):
    for pod in pods:
        melhor_worker = None
        melhor_score = -1

        for w in workers:
            if w.pode_alocar(pod):
                score = calcular_score(w)
                if score > melhor_score:
                    melhor_score = score
                    melhor_worker = w

        if melhor_worker:
            melhor_worker.alocar(pod)
            print(f"{pod.nome} → {melhor_worker.nome}")
        else:
            print(f"{pod.nome} NÃO ALOCADO")

workers = [
    Worker("Worker1", 16, 32, 100, 10),
    Worker("Worker2", 12, 16, 80, 20)
]

pods = []
for i in range(15):
    pods.append(Pod(
        f"Pod{i}",
        cpu=random.randint(1,4),
        memoria=random.randint(1,8),
        disco=random.randint(5,20)
    ))

escalonar(pods, workers)

print("\nEstado final:")
for w in workers:
    print(f"\n{w.nome}")
    print("Pods:", [p.nome for p in w.pods])
    print(f"CPU livre: {w.cpu}")
    print(f"Memória livre: {w.memoria}")
    print(f"Disco livre: {w.disco}")