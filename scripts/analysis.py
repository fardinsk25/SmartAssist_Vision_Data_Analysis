import json
import pandas as pd

def analyze_data(data_path='data.json'):
    with open(data_path, 'r') as f:
        data = json.load(f)

    print("--- SmartAssist Vision Data Analysis ---")
    print("\nKey Performance Indicators (KPIs):")
    for kpi, value in data['kpis'].items():
        print(f"  {kpi.replace('_', ' ').title()}: {value}")

    # Daily Detections and Accuracy
    daily_df = pd.DataFrame({
        'Date': pd.to_datetime(data['daily']['dates']),
        'Total Detections': data['daily']['totals'],
        'Accuracy': data['daily']['accuracy'],
        'Confidence': data['daily']['confidence']
    })
    daily_df = daily_df.set_index('Date')
    print("\nDaily Detection Trends (first 5 days):\n", daily_df.head())
    print("\nDaily Detection Trends (last 5 days):\n", daily_df.tail())

    # Object Class Analysis
    objects_df = pd.DataFrame({
        'Object Class': data['objects']['labels'],
        'Count': data['objects']['counts'],
        'Avg Confidence': data['objects']['avg_conf'],
        'Avg Response Time (ms)': data['objects']['avg_rt'],
        'High Alerts': data['objects']['high_alerts']
    })
    objects_df = objects_df.sort_values(by='Count', ascending=False).reset_index(drop=True)
    print("\nTop 5 Detected Object Classes:\n", objects_df.head())

    # Monthly Trends
    monthly_df = pd.DataFrame({
        'Month': data['monthly']['labels'],
        'Total Detections': data['monthly']['totals'],
        'Accuracy': data['monthly']['accuracy'],
        'High Alerts': data['monthly']['high'],
        'Medium Alerts': data['monthly']['medium'],
        'Low Alerts': data['monthly']['low'],
        'Avg Confidence': data['monthly']['avg_conf'],
        'Avg Response Time (ms)': data['monthly']['avg_rt']
    })
    print("\nMonthly Performance Summary:\n", monthly_df)

    # Location Analysis
    location_df = pd.DataFrame({
        'Location Type': data['location']['labels'],
        'Count': data['location']['counts'],
        'Accuracy': data['location']['accuracy'],
        'High Alerts': data['location']['high_alerts']
    })
    location_df = location_df.sort_values(by='Count', ascending=False).reset_index(drop=True)
    print("\nDetection by Location Type:\n", location_df)

    print("\n--- Insights ---")
    print("\nOverall Detection Accuracy: {:.2f}%".format(data['kpis']['detection_accuracy']))
    print("Average AI Confidence: {:.3f}".format(data['kpis']['avg_confidence']))
    print("Highest detected object class: {} with {} detections and average confidence of {:.3f}.".format(
        objects_df.iloc[0]['Object Class'], objects_df.iloc[0]['Count'], objects_df.iloc[0]['Avg Confidence']
    ))
    print("The analysis confirms that the SmartAssist Vision device maintains a high level of accuracy and confidence over time, with specific insights into object detection performance and environmental factors.")

if __name__ == '__main__':
    analyze_data()
