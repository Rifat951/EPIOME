declare -a array=("EX" "IP" "ER")
arrLen=${#array[@]}
# shellcheck disable=SC2004
for (( i=1; i<${arrLen} + 1; i++ ));
do
  if [[ $1 = "reddit" ]]; then
    python3 src/train.py \
      --train_path="dataset/reddit_model_${array[$i]}.csv" \
      --lr=2e-5 \
      --batch_size=32 \
      --lambda_EI=1.0 \
      --lambda_RE=0.5 \
      --save_model \
      --save_model_path="output/reddit_${array[$i]}.pth"
  else
    echo "Processing ${array[$i]} File"
    python3 src/train.py \
      --train_path="dataset/sample_input_model_${array[$i]}.csv" \
      --lr=2e-5 \
      --batch_size=32 \
      --lambda_EI=1.0 \
      --lambda_RE=0.5 \
      --do_validation=True \
      --do_test=True \
      --save_model \
      --save_model_path="output/sample_${array[$i]}.pth"
  fi
done