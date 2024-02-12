sudo docker stop personal-portfolio-container
sudo docker rm personal-portfolio-container
sudo docker build . -t 'personal-portfolio-image:2024'
sudo docker run --name personal-portfolio-container -d -it -p 9090:8000 --mount type=bind,source="$(pwd)",target=/core personal-portfolio-image:2024