from methods import*
train_df = pd.read_csv('/Users/anne/PycharmProjects/Semester4/machine_learning/semester_project'
                          '/breast-cancer_train.csv')


norm_df = load_and_normalize_data('/Users/anne/PycharmProjects/Semester4/machine_learning/semester_project'
                          '/breast-cancer_train.csv')

norm_train_df, norm_valid_df = split_data(norm_df, validation_size=0.33)

generate_pie_chart(norm_df)

generate_heatmaps(norm_train_df, norm_valid_df)

stats = get_statistics(train_df)
print(stats)
print(" ")
print(50 * "-")

relevant_features = get_relevant_features(norm_train_df, threshold=45)
print(" ")
print(50 * "-")

relevant_feature_df, valid_relevant_feature_df = get_relevant_feature_dfs(norm_train_df, norm_valid_df, relevant_features)

plot_relevant_features(relevant_feature_df, relevant_features)

w1, w0, error_list = train_model(relevant_feature_df.iloc[:,:-1].values, relevant_feature_df.loc[:,"diagnosis"].values, eta=0.05)
print(" ")
print(f"gewichtungsfaktor w1 pro Spalte: {w1}")
print(" ")
print(f"bias w0: {w0}")
print(50 * "-")

generate_error_plot(error_list)