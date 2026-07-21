import sys

def main():
    s1 = "교양이를 부탁해"
    s2 = "미래채널"
    s3 = "조코딩 JoCoding"
    s4 = "우왁굳"
    
    # Let's see what happens when we encode in utf-8 and decode in cp949
    for s in [s1, s2, s3, s4]:
        try:
            val = s.encode('utf-8').decode('cp949', errors='replace')
            print(f"Original: {s}")
            print(f"Decoded:  {val}")
            print("-" * 20)
        except Exception as e:
            print(f"Error for {s}: {e}")

if __name__ == "__main__":
    main()
