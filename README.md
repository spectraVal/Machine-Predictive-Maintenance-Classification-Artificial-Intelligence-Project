# Machine Maintenance Failure Classification

Penelitian ini menggunakan metode Multiclass Classification yang diawasi untuk memprediksi berbagai jenis kegagalan pemeliharaan mesin. Random Forest dengan class_weight dipilih sebagai model terakhir untuk mengatasi ketidakseimbangan kelas yang sangat besar.
Eksperimen dasar (Logistic Regression dan Desicion Tree) disertakan untuk perbandingan dan hasil akhir dibekukan menggunakan satu kali eksekusi yang dapat diulang.

## Dataset Characteristic

- Highly imbalanced multiclass dataset
- Majority class: No Failure
- Minority classes include: - Heat Dissipation Failure - Overstrain Failure - Power Failure - Tool Wear Failure - Random Failures
  Because of this imbalance, accuracy is not the primary metric.

## Final Model Configuration

```
|-----------------------------------------------|
|   Paramater               | Value             |
|:--------:--------:-------:|:--------:--------:|
|   Model                   | Random Forest     |
|   Train/Test Split        | 80/20             |
|   Class Weight            | Balanced          |
|   Hyperparameter Tuning   | None              |
|   Random State            | Fixed             |
|   Execution               | Single final run  |
|-----------------------------------------------|
```

## How to Run

Dalam proyek ini, ada dua metode eksekusi yang dapat dipilih peninjau.

---

### Option 1 — Recommended (One-Click Execution)

Untuk menjalankan eksperimen akhir dengan aman, gunakan berkas "run.bat" yang disediakan.

Pastikan Python dan virtual environment tersedia, jika belum silahkan:

```
pip install -r requirements.txt
```

**Steps:**

1. Pastikan Python dan virtual environment tersedia
2. Double-click `run.bat`
   Skrip ini akan melakukan hal-hal berikut:

- Menggunakan iterpreter Python yang benar dari virtual environment
- Menjalankan frozen final experiment
- Menyimpan semua output ke folder `outputs/`

Jika reviewer ingin melakukan eksperimen tanpa command line, metode ini akan sangat membantu.

---

### Option 2 — Manual Execution (Command Line)

Untuk pengguna yang lebih suka melakukan eksekusi langsung melalui command line, berikut step by stepnya:

```bash
pip install -r requirements.txt
venv\Scripts\python.exe -m final_run.main_final
```

Jika ingin menjalankan file eksperimen atau keseluruhan percobaan, silahkan:

```bash
venv\Scripts\python.exe -m experiments.run_experiments
```

Jika ingin menjalankan fitur visualisasi dari program ini, silahkan:

```bash
venv\Scripts\python.exe src/visualization/generate_all.py
```

## Output Files

All outputs are saved in:

```bash
outputs/
```

```
|-------------------------------------------------------------------|
|File Name                  | Description                           |
|:--------:--------:-------:|:--------:--------:--------:--------:--|
|prediction_results.csv     | Actual vs predicted labels            |
|classification_report.csv  | Precision, recall, F1-score per class |
|confusion_matrix.csv       | Numeric confusion matrix              |
|model_config.csv           | Final model parameters                |
|-------------------------------------------------------------------|
```

## Evaluation Notes

- Macro F1-score digunakan untuk mengevaluasi kinerja keseluruhan pada Multiclass Classification
- Beberapa kelas minoritas menerima prediksi nol akibat jumlah sampel yang sangat rendah
- Hal tersebut mencerminkan keterbatasan data, bukan kesalahan implementasi.

## Conclusion

Model Random Forest akhir menunjukkan kinerja yang kuat pada kelas mayoritas sambil menyoroti tantangan dalam deteksi kegagalan yang jarang terjadi. Proyek ini menekankan reproduibilitas, kejujuran metodologis, dan evaluasi yang transparan.
