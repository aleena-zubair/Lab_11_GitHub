# Storage Estimator
files = int(input("Number of files: "))
size_mb = float(input("Average file size in MB: "))
total_mb = files * size_mb
print("Estimated storage needed:", total_mb, "MB")
print("Estimated storage needed (GB):", total_mb / 1024)