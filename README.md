# ddos-regression-analysis
This project is primarily made to practice building classical machine learning on security data.
It consists of two models:
1) A behavioral fingerprint of DDoS traffic, by analyzing the pattern of packet length and number of packets. It uses a univariable linear regression model to predict the expected volume (total size of packets) based on the number of packets.
2) A classifier of DDoS traffic, using a regularized logistic regression model that classifies DDoS vs benign traffic based on the Packet Length Mean and Bwd Packet Length Mean (the size of packets in the backward direction of a data flow).
   
Both models are built on the intrusion detection evaluation dataset (CIC-IDS2017) by the Canadian Institute for Cybersecurity (https://www.unb.ca/cic/datasets/ids-2017.html). Exact sample used is the Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv.

