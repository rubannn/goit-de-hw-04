from spark_config import DATA_PATH, create_spark_session


def run() -> None:
    spark = create_spark_session()

    nuek_df = (
        spark.read
        .option("header", "true")
        .option("inferSchema", "true")
        .csv(DATA_PATH)
    )

    nuek_repart = nuek_df.repartition(2)

    nuek_processed = (
        nuek_repart
        .where("final_priority < 3")
        .select("unit_id", "final_priority")
        .groupBy("unit_id")
        .count()
    )

    # Проміжний action: collect
    nuek_processed.collect()

    # Ось ТУТ додано рядок
    nuek_processed = nuek_processed.where("count>2")

    nuek_processed.collect()

    input("Press Enter to continue...")

    spark.stop()


if __name__ == "__main__":
    run()
