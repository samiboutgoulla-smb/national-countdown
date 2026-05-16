import os

base_path = os.path.expanduser("~/countdown/2025 AVEC RÉGIONS")

subjects_map = {
    "AR": "arabe.pdf",
    "EI": "islamique.pdf",
    "FR": "francais.pdf",
    "HG": "histoire-geo.pdf"
}

def clean_project():
    if not os.path.exists(base_path):
        print(f"Dossier introuvable : {base_path}")
        return

    for region in os.listdir(base_path):
        region_path = os.path.join(base_path, region)
        if not os.path.isdir(region_path):
            continue
            
        print(f"✨ Traitement de la région : {region}")

        # 1. Standardisation du dossier de correction
        old_corr = os.path.join(region_path, "الإجابة")
        new_corr = os.path.join(region_path, "عناصر الإجابة")
        if os.path.exists(old_corr) and not os.path.exists(new_corr):
            os.rename(old_corr, new_corr)
        
        # 2. Renommage dans "المواضيع"
        subj_folder = os.path.join(region_path, "المواضيع")
        if os.path.isdir(subj_folder):
            for f in os.listdir(subj_folder):
                for code, clean in subjects_map.items():
                    if f.startswith(code) and f.endswith(".pdf") and f != clean:
                        os.rename(os.path.join(subj_folder, f), os.path.join(subj_folder, clean))
                        print(f"  [Sujet] Renommé : {f} -> {clean}")

        # 3. Renommage dans "عناصر الإجابة"
        corr_folder = os.path.join(region_path, "عناصر الإجابة")
        if os.path.isdir(corr_folder):
            for f in os.listdir(corr_folder):
                for code, clean in subjects_map.items():
                    if f.startswith(code) and f.endswith(".pdf") and not f.startswith("corr_"):
                        target_name = f"corr_{clean}"
                        os.rename(os.path.join(corr_folder, f), os.path.join(corr_folder, target_name))
                        print(f"  [Corr] Renommé : {f} -> {target_name}")

if __name__ == "__main__":
    clean_project()
    print("\nTous les fichiers de toutes les régions sont prêts et synchronisés !")