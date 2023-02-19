from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

# Estructura de la red incluyendo los arcos y nodos
model_2 = BayesianNetwork([("R", "A"), ("S", "A"), ("A", "J"), ("A", "M")])

# CPD: Conditional Probability Distribution
# CPDs de R y S
cpd_r = TabularCPD(
    variable="R",
    variable_card=2,
    values=[[0.01], [0.99]])
cpd_s = TabularCPD(
    variable="S",
    variable_card=2,
    values=[[0.02], [0.98]])

# CPD de A
cpd_al = TabularCPD(
    variable="A",
    variable_card=2,
    values=[
        [0.95, 0.94, 0.29, 0.001],
        [0.05, 0.06, 0.71, 0.999],
    ],
    evidence=["R", "S"],
    evidence_card=[2, 2])

# CPD de J
cpd_j = TabularCPD(
    variable="J",
    variable_card=2,
    values=[
        [0.9, 0.05],
        [0.1, 0.95],
    ],
    evidence=["A"],
    evidence_card=[2])

# CPD de M
cpd_m = TabularCPD(
    variable="M",
    variable_card=2,
    values=[
        [0.7, 0.01],
        [0.3, 0.99],
    ],
    evidence=["Al"],
    evidence_card=[2],
)

# Asocie las 5 CPDs a su modelo

model_2.add_cpds(cpd_r, cpd_s, cpd_al, cpd_j, cpd_m)

# Revise que su modelo este completo

model_2.check_model()
