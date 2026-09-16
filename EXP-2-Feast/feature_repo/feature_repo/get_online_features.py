from feast import FeatureStore

store = FeatureStore(repo_path=".")

features = store.get_online_features(
    features=[
        "student_features:attendance",
        "student_features:assignment_score",
        "student_features:internal_mark",
    ],
    entity_rows=[
        {"student_id": 101}
    ],
).to_dict()

print("Online Features for Student 101:")
print(features)