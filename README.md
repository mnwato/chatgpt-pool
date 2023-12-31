# **chatgpt-pool**: Free and easy access to ChatGPT
**ChatGPT Pool** is a pool of ChatGPT (official and free) reverse proxy services.
- The idea for this package arises from a text annotation task that requires thousands of requests.
- The goal is to have a pool of ChatGPT instances to decrease the probability of getting blocked.


## Usage:
- Data annotation
- Access to free chatGPT services.
- Access to many chatGPT services using single class.

## TODO:
- [x] Support find first available service in the pool
- [x] Request to sepecific service
- [ ] Support history for official OpenAI
- [ ] Add more ChatGPT services
- [ ] You suggest

## List of services:
<table>
    <thead>
    <tr>
        <th></th>
        <th>Url</th>
        <th>Service name</th>
        <th>Status</th>
        <th>Supported models</th>
    </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td> <a href="https://chat.openai.com" target="_blank">https://chat.openai.com</a>
                <br> </td>
            <td>openai</td>
            <td>✔️</td>
            <td>
                <details>
                    <summary>Click to expand</summary>
                    <ul>
                        <li>gpt-3.5-turbo</li>
                        <li>gpt-3.5-turbo-16k</li>
                        <li>gpt-4</li>
                        <li>gpt-4-32k</li>
                        <li>text-davinci-003</li>
                        <li>text-curie-001</li>
                        <li>text-babbage-001</li>
                        <li>text-ada-001</li>
                    </ul>
                </details>
            </td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td>2</td>
            <td> <a href="https://gptgo.ai" target="_blank">https://gptgo.ai/?hl=en</a>
                <br> </td>
            <td>gpt_go</td>
            <td>✔️</td>
            <td>gpt-3.5-turbo</td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td>3</td>
            <td> <a href="https://easygpt.io" target="_blank">https://easygpt.io</a>
                <br> </td>
            <td>easy_gpt</td>
            <td>✖️</td>
            <td>gpt-3.5-turbo</td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td>4</td>
            <td> <a href="https://p5.v50.ltd" target="_blank">https://p5.v50.ltd</a>
                <br> </td>
            <td>p5_v50</td>
            <td>✔️</td>
            <td>
                <details>
                    <summary>Click to expand</summary>
                    <ul>
                        <li>gpt-3.5-turbo</li>
                        <li>gpt-3.5-turbo-0301</li>
                        <li>gpt-3.5-turbo-0613</li>
                        <li>gpt-3.5-turbo-16k</li>
                        <li>gpt-3.5-turbo-16k-0613</li>
                        <li>gpt-4</li>
                        <li>gpt-4-0613</li>
                    </ul>
                </details>
            </td>
        </tr>
    </tbody>

</table>

<br/><br/>

## How to Use:
1. Edit **model_configs.json** in root path, for example:    
    Set your OpenAI API info if you want to use OpenAI models:
     ```JSON
        "openai": {
            "OPENAI_API_KEY": "YOUR_OPENAI_API_KEY",
            "OPENAI_ORG_KEY": "YOUR_OPENAI_ORG_KEY",
            "OPENAI_Model_Name": "gpt-3.5-turbo"
        }
2. There are example codes in root:
    - You can use your prefered service name to request ChatGPT:    
        `/example/single_service.py`
    - Find available service:   
        `/example/find_availabe_service.py`