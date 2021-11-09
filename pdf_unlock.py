import pikepdf

path = r"D:\ORACLE\Oracle Content\Documentos_oci\MACHINE_LEARNING-20211027T223702Z-001\MACHINE_LEARNING\D105137GC10_ag.pdf"

path_limpio = r"D:\ORACLE\Oracle Content\Documentos_oci\MACHINE_LEARNING-20211027T223702Z-001\MACHINE_LEARNING\D105137GC10_ag_sin.pdf"

pdf = pikepdf.open(path)
pdf.save(path_limpio)
print("done")