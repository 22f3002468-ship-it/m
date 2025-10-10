# Latency Metrics API

This is a FastAPI application that provides latency metrics based on region.

## Description

The API receives a POST request with a list of regions and a latency threshold. It then reads latency data from a JSON file, calculates average latency, 95th percentile latency, average uptime, and the number of latency breaches for each specified region.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   uvicorn app:app --reload
   ```

2. Send a POST request to the `/` endpoint with a JSON body like this:
   ```json
   {
     "regions": ["iad1", "sfo1"],
     "threshold_ms": 100
   }
   ```

This will return a JSON response with the calculated metrics for the specified regions.
