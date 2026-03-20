import torch
import os
import csv
from baseline.train import main as train_main  # adjust if train.py uses a different entry

# -------------------------
# CPU-only configuration
# -------------------------
device = 'cpu'
tokens_per_iter = 16384

# Optional: override any baseline config defaults here
config_overrides = {
    'device': device,
    'tokens_per_iter': tokens_per_iter,
}

# -------------------------
# Run baseline
# -------------------------
# Assuming train.py supports a dict of config overrides
# If not, you can modify train.py to accept these arguments
train_main(config_overrides)

# -------------------------
# Log results automatically
# -------------------------
log_file = os.path.join("..", "logs", "experiment_log.csv")
final_loss = 0.0  # replace with actual value from train_main if accessible

# Write header if file is empty
if not os.path.exists(log_file):
    with open(log_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['run','learning_rate','batch_size','predicted_score','actual_score','notes'])

# Append first run
with open(log_file, 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([1,'default','default','','{:.4f}'.format(final_loss),'CPU baseline'])
