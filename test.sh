if [[ $1 = "reddit" ]]; then
    python3 src/test.py \
      --input_path dataset/sample_test_input.csv \
      --output_path output/reddit_test_output.csv \
      --ER_model_path output/reddit_ER.pth \
      --IP_model_path output/reddit_IP.pth \
      --EX_model_path output/reddit_EX.pth
else
    python3 src/test.py \
      --input_path dataset/sample_test_input.csv \
      --output_path output/sample_test_output.csv \
      --ER_model_path output/sample_ER.pth \
      --IP_model_path output/sample_IP.pth \
      --EX_model_path output/sample_EX.pth
fi