from update_content import update_document_content, upload_image_to_firebase
from file_converter import convert_pdf_to_jpg
from downloader import download_doc_as_pdf
from spaceandtime import send_sql
from poe import send_prompt


async def fetch_sql_data(query):
    # Wrapping send_sql in an async function to await its result
    return send_sql(query)


async def main(query, example):
    result_of_sql = await fetch_sql_data(query)
    print(result_of_sql)
    await send_prompt(example + result_of_sql)


if __name__ == '__main__':
    ethereum = "Ethereum"
    query = """--Give me transaction count ethereum in each day of the last 623 days
SELECT 
    DATE(time_stamp) AS transaction_date, 
    COUNT(*) AS transaction_count
FROM 
    ETHEREUM.TRANSACTIONS
WHERE 
    time_stamp BETWEEN date_sub(CAST('2024-10-29' AS DATE), 623) AND CAST('2024-10-29' AS TIMESTAMP)
GROUP BY 
    DATE(time_stamp)
ORDER BY 
    transaction_date ASC LIMIT 100;"""
    example = f"""Example1:
Ethereum, like a dense forest floor, supports complex life but requires higher resources to thrive. Fewer but significant transactions represent the early organisms of the blockchain’s complex ecosystem.
Example2:
zkSync symbolizes new sprouts emerging in fresh soil—numerous smaller transactions bloom as the environment encourages rapid participation.

Example3:
High gas fees in Ethereum represent fierce competition for resources in a mature ecosystem, with only the most resource-rich entities able to flourish.
Example4:
zkSync, like an adaptive ecosystem, offers an abundant environment with lower gas fees, allowing more organisms (users) to thrive.

Example5:
Ethereum operates like a large, ancient tree—slow and steady, supporting complex structures but with limited agility.
Example6:
zkSync’s throughput resembles fast-moving animals evolving to survive—able to handle rapid transactions without congestion.

 It is {ethereum}. You have to generate a short header and description to this data according to those examples. remake this according to the data that i will feed you with . Perceive all the fancy wordings, style and storytelling. Give only text, don't include graphs. Give me header and description only but don't dive into details of the graph.
"""
    import asyncio
    asyncio.run(main(query, example))
    for i in range(1, 13):
        if_dark = False
        if not i % 2:
            if_dark = True
        header_text = ""
        body_text = ""
        doc_id = update_document_content(i, if_dark)
        download_doc_as_pdf(doc_id=doc_id, output_path=f"IMG{i}.pdf")
        convert_pdf_to_jpg(f"IMG{i}.pdf", f"IMG{i}.png")
        firebase_url = upload_image_to_firebase(f"IMG{i}.png")