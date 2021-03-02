"""Training script test suite."""
from jarvisdgl.main import train_property_model
from jarvisdgl.train import train_dgl


def test_prop():
    """Test full training run with small batch size."""
    train_property_model(epochs=2, maxrows=16, batch_size=8)

config_d={
  "dataset": "dft_3d",
  "target": "formation_energy_peratom",
  "random_seed": 123,
  "n_val": 7200,
  "n_train": 28800,
  "epochs": 100,
  "batch_size": 256,
  "weight_decay": 0,
  "learning_rate": 0.01,
  "criterion": "mse",
  "atom_features": "basic",
  "optimizer": "adamw",
  "conv_layers": 3,
  "edge_features": 16,
  "node_features": 64,
  "fc_layers": 1,
  "fc_features": 128,
  "output_features": 1,
  "logscale": False
}

def test_cgcnn_ignite():
    """Test CGCNN end to end training."""
    config = dict(
        target="formation_energy_peratom",
        epochs=2,
        n_train=16,
        n_val=16,
        batch_size=8,
    )
    result = train_dgl(config_d)
    print(result)
test_cgcnn_ignite()
