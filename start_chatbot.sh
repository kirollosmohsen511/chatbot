#!/bin/bash
echo "================================"
echo " Blood Donation Chatbot Starting"
echo "================================"
cd ~/Downloads/chat2
echo ""
echo "Installing requirements..."
pip3 install -r requirements.txt
echo ""
echo "Starting server..."
python3 -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload

